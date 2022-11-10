import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";
import { Link } from "react-router-dom";

function OutingsPage() {
  const [outings, setOutings] = useState("");
  const api = useAxios();
  const { user } = useContext(AuthContext)
  
  const calculateUserExpenses = (expenseType, data) => {
    const expenses = data.map(outing => {
      const expensesArr = outing.expenses.map((expense) => {
        if ((expense.paid_for.id !== expense.paid_by.id)&&(expense[`${expenseType}`].id === user.profile.id)) {
          return expense.value
        } else return 0
      })
      return expensesArr
    });
    const expensesSum = expenses.map(expenses => {
      return expenses.reduce((a, b) => { return a + b }, 0)
    });
    return expensesSum
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/outings/outings/");
        const expensesList = response.data.map(outing => {
          return outing.expenses.map(expense => expense.value)
        });
        const expensesSum = expensesList.map(expenses => {
          const expensesSummed = expenses.reduce((a, b) => { return a + b }, 0)
          return expensesSummed
        });
        

        response.data.map((outing, index) => {
          outing['owedByUser'] = calculateUserExpenses("paid_for", response.data)[index]
          outing['owedToUser'] = calculateUserExpenses("paid_by", response.data)[index]
          return outing['totalExpense'] = expensesSum[index]
        });

        console.log(user)
        setOutings(response.data);
      } catch {
        setOutings("Something went wrong");
      }
    };
    fetchData();

    
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div>
      <h1>Protected Page</h1>
      {outings ? outings.map((outing, key) => (
        <div key={key}>
          <h3>{outing.title}</h3>
          <p>{outing.place}</p>
          <small>{outing.date}</small>
          <p>Number of participants: {outing.participants.length}</p>
          <Link to={`/outings/${outing.id}`} state={{ outing: outing }}>Details</Link>
          {outing.owedByUser ? <strong>You owe money! </strong> : ""}
          {outing.owedToUser?<strong>Someone owes you money!</strong>:"" }
          
        </div>
        
      )):"loading"}
    </div>
  );
}

export default OutingsPage;