import React from 'react';
import './Board.css';

function Board(props) {
  return (
    <div className={props.turn=='X'?"board red-turn":"board blue-turn"}>
      {props.board.map((row, rowIndex) => (
        <div key={rowIndex} className="row">
          {row.map((cell, colIndex) => (
            <div key={colIndex} className={"cell "+cell} onClick={() => props.onClick(colIndex)}>
              {cell}
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default Board;
