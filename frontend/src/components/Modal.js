import {React, useState, useEffect} from 'react'

export default function Modal({ content, isModalOpen, changeModalStatus }) {


    return (
    <>
        {isModalOpen?<div className='overlay' >
            <div className='modal-container'>
                <span onClick={()=>changeModalStatus()} className='modal-close'>x</span>
                {content}
            </div>
      </div >:""}
      </>
  )
}
