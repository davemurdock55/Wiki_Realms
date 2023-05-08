import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

interface RealmInfo {
  title: string;
  description: string;
  image: string;
}

export default function Realm() {
  const { id } = useParams();
  const [realm, setRealm] = useState<RealmInfo>({
    title: "",
    description: "",
    image: "",
  });

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/realms/${id}/`)
      .then((response) => {
        setRealm(response.data);
      })
      .catch((error) => console.error(error));
  }, [id]);

  return (
    <div className="relative h-screen">
      <img
        className="absolute top-0 w-full h-1/2 object-cover"
        src={realm.image}
        alt={realm.title}
      />
      <h1 className="absolute top-1/4 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-white text-6xl font-bold shadow-2xl">
        {realm.title}
      </h1>
    </div>
  );
}
