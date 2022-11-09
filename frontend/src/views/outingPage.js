import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";
import { useParams } from "react-router-dom";

function OutingPage() {
  const [outing, setOuting] = useState("");
  const api = useAxios();
  const { user } = useContext(AuthContext)
  const { id } = useParams()

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get(`/outings/outings/${id}`);
        console.log(response.data)
        setOuting(response.data);
      } catch {
        setOuting("Something went wrong");
      }
    };
    console.log(user)
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

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
          )):<li>No expenses added so far</li>}
          </ul>
        </div>
      </div>:"loading"}
    </div>
  );
}

export default OutingPage;