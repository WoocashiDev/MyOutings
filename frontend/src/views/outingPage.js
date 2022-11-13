import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";
import { useParams} from "react-router-dom";
import Modal from "../components/Modal"
import EditExpense from "../components/EditExpense";

function OutingPage() {
  const api = useAxios()
  const { user } = useContext(AuthContext)
  const { id } = useParams()

  const [outing, setOuting] = useState("");
  const [updating, setUpdating] = useState(false)
  
  const calculateUserExpenses = (expenseType, data) => {
    const expenses = data.expenses.map((expense) => {
      if ((expense.paid_for.id !== expense.paid_by.id) && (expense[`${expenseType}`].id === user.profile.id)) {
          console.log(expense.value)
            return expense.value
        } else return 0
    })
    const expensesSum = expenses.reduce((a, b) => { return a + b }, 0)
    return expensesSum
}

useEffect(() => {
    const fetchData = async () => {
        try {
          const response = await api.get(`/outings/outings/${id}/`);
          const data = response.data;
          const expensesList = data.expenses.map(expense => (expense.value))
          const expensesSum = expensesList.reduce((a, b) => { return a + b }, 0)     
            data['owedByUser'] = calculateUserExpenses("paid_for", data)
            data['owedToUser'] = calculateUserExpenses("paid_by", data)
            data['totalExpense'] = expensesSum
            setOuting(data);
        } catch {
            setOuting("Something went wrong");
        }
    };
    fetchData();  
    // eslint-disable-next-line react-hooks/exhaustive-deps
}, [updating]);
console.log(outing)


  // handling modal status
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [modalContent, setModalContent] = useState({})

  const handleModalStatus = (content) => {
    if (content) {
      setUpdating(true)
      setModalContent(()=>content)
      setIsModalOpen(!isModalOpen)
    } else {
      setUpdating(false)
      setIsModalOpen(false)
    }
  }


  return (
    <main>
      <h1 className="title-primary">Outing details</h1>
      {outing ? <><div className="cards gap-40">
        <div className="card gap-20">
          <div>
            <h3 className="card-title">{outing.title}</h3>
            <span className="card-date">On: {outing.date}</span>
          </div>
          <div>
            <h4 className="title-secondary">Place:</h4>
            <span className="data-primary">{outing.place}</span>
          </div>
          {/*PARTICIPANTS*/}
        <div>
          <h4 className="title-secondary">Participants:</h4>
          <div className="card-participants">
            {outing.profiles.map((participant, key) => (
              <div key={key}>
                <div className="card-participant">
                  {participant.nickname}
                  <button onClick={() => handleModalStatus(<div>test content{key }</div>)}>X</button>
                </div>
              </div>
            ))}
          </div>
        </div>
          <div>
            {/*SUMMARY*/}
          <div>
            <h4 className="title-secondary">Summary:</h4>
            <ul className="card-summary">
              <li>Total outing cost: <span className="data-primary">{outing.totalExpense}</span></li>
                <li>You owe: <span className="data-primary">{outing.owedByUser}</span>
                </li>
                <li>Others owe to you: <span className="data-primary">{outing.owedToUser}</span>
                </li>
            </ul>
          </div>
        </div>
        </div>

        {/*EXPENSES*/}
          <div className="card">
            <h4 className="title-secondary">Expenses:</h4>
            {outing.expenses.length > 0 ? <table className="card-table">
              <tr>
                <th>Item</th>
                <th>Price</th>
                <th>For</th>
                <th>Paid By</th>
                <th><span onClick={() => handleModalStatus(<div>test content</div>)} className="card-button-round center">+</span></th>
              </tr>
              {outing.expenses.map((expense,key) => (
                <tr key={key}>
                <td>{expense.title}</td>
                <td>{expense.value}</td>
                <td>{expense.paid_for.nickname}</td>
                  <td>{expense.paid_by.nickname}</td>
                  <td><span onClick={() => handleModalStatus(<EditExpense participants={outing.profiles} expense={expense} closeModal={()=>handleModalStatus()} />)}  className="card-button">Edit</span></td>
                </tr>
            ))}
            </table> :<p>No expenses added so far</p>}
          </div> 
        {/*UPDATE DATE*/}
        <span className="card-date">Last updated on: {outing.updated}</span>
      </div>
        <Modal isModalOpen={isModalOpen} changeModalStatus={setIsModalOpen} content={modalContent} />
        </> : <div>"loading"</div>}
    </main>
  );
}

export default OutingPage;