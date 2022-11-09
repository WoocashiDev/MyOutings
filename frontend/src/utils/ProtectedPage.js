import { useEffect, useState } from "react";
import useAxios from "../utils/useAxios";
import { useContext } from 'react';
import AuthContext from "../context/AuthContext";

function ProtectedPage() {
  const [res, setRes] = useState("");
  const api = useAxios();
  const {user} = useContext(AuthContext)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/outings/outings/");
        console.log(response.data)
        setRes(response.data);
      } catch {
        setRes("Something went wrong");
      }
    };
    console.log(user)
    fetchData();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div>
      <h1>Protected Page</h1>
      {res ? res.map((item, key) => (
        <div key={key}>
          <h3>{item.title}</h3>
          <p>{item.place}</p>
          <small>{ item.date}</small>
        </div>
        
      )):"loading"}
    </div>
  );
}

export default ProtectedPage;