import { useState, useEffect } from 'react'

export default function APP() {
  const [data, setData] = useState("");

  useEffect (() => {
    fetch("http://localhost:8000/api/data")
    .then((response) => response.json())
    .then((data) =>  setData(data.data));
  }, []);

  return(
    <div>
      <h1> KTiPs Python React</h1>
      <p>{data}</p>
    </div>
  )
}