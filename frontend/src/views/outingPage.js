import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";
import { useParams, useLocation } from "react-router-dom";

function OutingPage() {

  const { user } = useContext(AuthContext)
  const { id } = useParams()
  const location = useLocation()
  const { outing } = location.state
  
  console.log(outing)

  return (
    <div>
      <h1>Outing details</h1>
      {outing ? <div>
        <h3>Title: {outing.title}</h3>
        <small>On: {outing.date}</small>
        <p>Place: {outing.place}</p>
        <p>Last updated on: {outing.updated}</p>
        <div>
          <h4>Participants:</h4>
          {outing.profiles.map((participant, key) => (
            <div key={key}>
              <small>{participant.nickname}</small><button>remove</button>
            </div>
          ))}
          <h4>Expenses</h4>
          <ul>
          {outing.expenses?outing.expenses.map((expense,key) => (
            <li key={key}>{expense.title} | cost: {expense.value} | paid by: {expense.paid_by.nickname} | paid for: { expense.paid_for.nickname }</li>
          ))
            : <li>No expenses added so far</li>}
          </ul>
          {outing.expenses ? <div>
            <h4>Summary:</h4>
            <ul>
              <li>Total outing cost: <strong>{outing.totalExpense}</strong></li>
              <li>You owe: <strong>{outing.owedByUser}</strong></li>
              <li>Others owe to you: <strong>{outing.owedToUser}</strong></li>
            </ul>
          </div>:""}
        </div>
      </div>:"loading"}
    </div>
  );
}

export default OutingPage;