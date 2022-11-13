import React, { useEffect, useRef, useState } from 'react';
import useAxios from '../utils/useAxios';


export default function EditExpense({expense, participants, closeModal}) {

  const api = useAxios()

  const activeInput = useRef(null)
  const handleFocus = () => {
    activeInput.current.focus()
  }


  useEffect(() => {
    handleFocus()
  }, [])
  
  const handleSubmit = (e) => {

    e.preventDefault()
    console.log(e.target.paidBy.value)
    console.log(e.target.paidFor.value)
    console.log(e.target.itemName.value)
    console.log(e.target.itemPrice.value)

    const fetchData = async () => {
      try {
        const response = await api.put(`/outings/outings/${expense.outing}/expenses/${expense.id}/update/`, {
          sponsor: e.target.paidBy.defaultValue,
          beneficient: e.target.paidFor.defaultValue,
          title: e.target.itemName.value,
          value: e.target.itemPrice.value,
        });
        console.log(response)
      } catch (error) {
        console.log(error)
      };
    }

    fetchData()
    closeModal()
  }

  return (
    <div className='form-container'>
      <h4 className='title-small'>Edit</h4>
      <form onSubmit={handleSubmit} className='form'>
        <div className='form-group'>
          <div className='form-field'>
            <label htmlFor="itemName">Item name</label>
            <input ref={activeInput} id="itemName" placeholder="item name" defaultValue={expense.title} type="text"/>
          </div>
          <div className='form-field'>
            <label htmlFor="itemPrice">Item price</label>
            <input id="itemPrice" defaultValue={expense.value} placeholder="item price" type="text"/>
          </div>
          <div className='form-field'>
            <label htmlFor="paidFor">Ordered by</label>
            <select value={ expense.paid_for.nickname} id="paidFor">
              {participants.map((profile, key) => (
                <option key={key} value={profile.id}>{profile.nickname}</option>
              ))}
            </select>
          </div>
          <div className='form-field'>
          <label htmlFor="paidBy">Paid by</label>
            <select id="paidBy">
              <option defaultValue="test">Test</option>
            </select>
          </div>
        </div>
        <input className='form-button' type="submit" value="Save"/>
      </form>
    </div>
  )
}
