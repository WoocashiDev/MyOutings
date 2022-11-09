import React from 'react';
import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";
import { useParams } from "react-router-dom";

export default function OutingParticipants() {
    const { participants, setParticipants } = useState([])
    const api = useAxios()
    const { user } = useContext(AuthContext)
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await api.get('/profiles')
            } catch {

            }
        }
    })

  return (
    <div>OutingParticipants</div>
  )
}
