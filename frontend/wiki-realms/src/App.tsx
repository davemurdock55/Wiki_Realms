import React from "react";
import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";
import RealmCard from "./components/RealmCard";

function App() {
  const [realms, setRealms] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/realms/")
      .then((response: any) => {
        setRealms(response.data["realms"]);
      })
      .catch((error: any) => console.error(error));
  }, []);

  return (
    <>
      <div className="flex flex-col items-center">
        <h1 className="my-10 text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-500 to-pink-500">
          Wiki Realms
        </h1>

        <button className="mb-10 relative inline-flex items-center justify-center p-0.5 mb-2 mr-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-500 to-pink-500 group-hover:from-purple-500 group-hover:to-pink-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800">
          <span className="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
            Test Button
          </span>
        </button>
      </div>

      {/* <div className="flex flex-wrap justify-center">
        <div className="rounded-lg shadow-lg m-4 p-6 basis-4/5">Card 1</div>
        <div className="rounded-lg shadow-lg m-4 p-6 basis-4/5">Card 2</div>
        <div className="rounded-lg shadow-lg m-4 p-6 basis-4/5">Card 3</div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-1 gap-4">
        <div className="rounded-lg shadow-lg p-6 mx-36">Card 1</div>
        <div className="rounded-lg shadow-lg p-6 mx-36">Card 2</div>
        <div className="rounded-lg shadow-lg p-6 mx-36">Card 3</div>
      </div> */}

      <div>
        {realms.length > 0 && (
          <>
            {/* <div className="flex flex-wrap justify-center"> */}
            {realms.map((realm) => (
              <RealmCard
                key={realm["id"]}
                title={realm["name"]}
                description={realm["description"]}
                url="#top"
                image={"http://127.0.0.1:8000/media/" + realm["image"]}
              />
            ))}
            {/* </div> */}
          </>
        )}
      </div>
    </>
  );
}

export default App;
