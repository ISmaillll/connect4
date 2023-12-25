import { io } from 'socket.io-client';
import { variables } from './Variables';

const socket = io(variables.backend_URL); // Replace with your server URL

class SocketService {
  static sendMessage(message) {
    socket.emit('message', message);
  }

  static onMessage(callback) {
    socket.on('message', callback);
  }
}

export default SocketService;
