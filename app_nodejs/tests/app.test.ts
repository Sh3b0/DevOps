import { io, Socket } from 'socket.io-client';
import { gameEnvType } from '../src/types';

describe('Game', () => {
  let p1: Socket;
  let p2: Socket;
  let gameEnv: gameEnvType;
  const roomName = Math.random().toString();

  beforeAll((done) => {
    const uri = `http://localhost:${process.env.PORT || 8080}`;
    p1 = io(uri);
    p2 = io(uri);
    p1.on('connect', () => {
      if (p2.connected) {
        done();
      }
    });
    p2.on('connect', () => {
      if (p1.connected) {
        done();
      }
    });
  });

  afterAll((done) => {
    if (p1.connected) {
      p1.disconnect();
    }
    if (p2.connected) {
      p2.disconnect();
    }
    done();
  });

  it('should create room on server', (done) => {
    p1.emit('joinRoom', { playerName: 'p1', roomName }, (error?: string) => {
      if (error) {
        done(error);
      }
    });

    p1.on('gameData', (data) => {
      gameEnv = data.gameEnv;
      done();
    });
  });

  it('should join existing room on server', (done) => {
    p2.emit('joinRoom', { playerName: 'p2', roomName }, (error?: string) => {
      if (error) {
        done(error);
      }
    });

    p2.on('gameData', () => {
      done();
    });
  });

  it('should change player1 location', (done) => {
    p1.emit('movePlayer', { playerNumber: 1, direction: 1, roomName });
    p1.on('locationUpdate', ({ playerNumber, newLocation }) => {
      if (playerNumber === 1) {
        expect(newLocation.y).toBeLessThan(gameEnv.p1Location.y);
        done();
      }
    });
  });

  it('should change player2 location', (done) => {
    p2.emit('movePlayer', { playerNumber: 2, direction: -1, roomName });
    p2.on('locationUpdate', ({ playerNumber, newLocation }) => {
      if (playerNumber === 2) {
        expect(newLocation.y).toBeGreaterThan(gameEnv.p2Location.y);
        done();
      }
    });
  });
});