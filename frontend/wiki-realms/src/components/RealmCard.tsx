import React from "react";

interface RealmCardProps {
  url: string;
  image: string;
  title: string;
  description: string;
}

export default function RealmCard(props: RealmCardProps) {
  return (
    <div className="flex flex-col items-center my-12">
      <a
        href={props.url}
        className="relative w-3/5 group border shadow-sm rounded-3xl overflow-hidden hover:shadow-xl transition"
      >
        <img
          className="object-cover object-center w-full h-96 rounded-3xl shadow-lg group-hover:scale-105 transition-transform duration-500 ease-in-out "
          src={props.image}
          alt=""
        />
        <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-gray-800/50 to-transparent rounded-b-3xl">
          <h3 className="text-3xl font-bold text-white">{props.title}</h3>
          <p className="mt-1 text-gray-300">{props.description}</p>
        </div>
      </a>
    </div>
  );
}
