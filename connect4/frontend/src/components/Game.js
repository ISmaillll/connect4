import React, { useState } from 'react';
import { useEffect } from 'react'; 
import Board from './Board';

function Game() {
  const [board, setBoard] = useState(Array(6).fill(Array(7).fill(null)));
  const [player, setPlayer] = useState('X');
  const [timeLeft, setTimeLeft] = useState(30);
  const [Running, setRunning] = useState(true);

  const handleMove = (col) => {
    const newBoard = board.map(row => [...row]);
    let i = newBoard.length-1;
    while (newBoard[i][col] !== null){
      i--;
      console.log(i)
    }
    if (i < 0) {
      return;
    }
    newBoard[i][col] = player;
    console.log(newBoard)
    setBoard(newBoard);
    setPlayer(player === 'X' ? 'O' : 'X');
    setTimeLeft(30);
  };
  const restart =()=>{
    const newBoard = Array(6).fill(Array(7).fill(null));
    setBoard(newBoard);
    setPlayer('X');
    setTimeLeft(30);
    setRunning(true);
  };
  const stopTimer = ()=>{
    setRunning(false)
  }
  const startTimer = ()=>{
    setRunning(true)
  }
  useEffect(() => {
    if(Running){
      if (timeLeft > 0 ) {
        const timer = setTimeout(() => setTimeLeft(prev => prev - 1), 1000);
        return () => clearTimeout(timer);
      } else {
        handleTurnEnd();
      }
    }
  }, [Running, timeLeft]);
  
  const handleTurnEnd = () => {
    const messages = ["Time's up!", "Out of time!", "Hurry up!"];
    alert(messages[Math.floor(Math.random() * messages.length)]);
    setPlayer(player === 'X' ? 'O' : 'X');
  };
  return (
    <div>
      <h1 className='text-light'>Connect Four</h1>
      <p className='text-light'>Time left: {timeLeft} seconds</p>
      {Running?<button onClick={stopTimer}>Pose</button>:<button onClick={startTimer}>Back</button>}
      <button onClick={restart}><i class="fa fa-refresh" aria-hidden="true"></i></button>
      <Board board={board} turn={player} onClick={handleMove} />
    </div>
  );
}

export default Game;
