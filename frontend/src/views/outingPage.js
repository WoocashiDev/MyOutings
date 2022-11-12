import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";
import { useParams, useLocation } from "react-router-dom";
import Modal from "../components/Modal"

function OutingPage() {

  const { user } = useContext(AuthContext)
  const { id } = useParams()
  const location = useLocation()
  const { outing } = location.state

  // handling modal status
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [modalContent, setModalContent] = useState({})
  const handleModalStatus = (content) => {
    setModalContent(()=>content)
    setIsModalOpen(!isModalOpen)
  }

  
  console.log(outing)

  return (
    <main>
      <h1 className="title-primary">Outing details</h1>
      {outing ? <div className="cards gap-40">
        <div className="card gap-20">
          <div>
            <h3 className="card-title">{outing.title}</h3>
            <span className="card-date">On: {outing.date}</span>
          </div>
          <div>
            <h4 className="title-secondary">Place:</h4>
            <span className="data-primary">{outing.place}</span>
          </div>
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
                  <td><span onClick={() => handleModalStatus(<div>test content</div>)}  className="card-button">Edit</span></td>
                </tr>
            ))}
            </table> :<p>No expenses added so far</p>}
          </div> 
        
        <span className="card-date">Last updated on: {outing.updated}</span>
      </div> : "loading"}
      <Modal isModalOpen={isModalOpen} changeModalStatus={setIsModalOpen} content={ modalContent } />
    </main>
  );
}

export default OutingPage;