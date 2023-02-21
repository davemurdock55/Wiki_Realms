import Head from 'next/head';
import Image from 'next/image';
import { Inter } from '@next/font/google';

import axios from 'axios';
import { useEffect, useState } from 'react';

import styles from '@/styles/Home.module.css';


const inter = Inter({ subsets: ['latin'] });



function Characters ()
{
     const [characters, setCharacters] = useState([]);

     useEffect(() =>
     {
          axios.get('http://127.0.0.1:8000/api/characters/')
               .then(response =>
               {
                    console.log(response.data['pages']);
                    setCharacters(response.data['pages']);
               })
               .catch(error => console.error(error));
     }, []);

     return (
          <>
               <Head>
                    <title>Characters</title>
                    <meta name="description" content="Generated by create next app" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" href="/favicon.ico" />
               </Head>
               <main className={ styles.main }>

                    <div className={ styles.center }>
                         <h1 className={ styles.title }>
                              Characters
                         </h1>
                    </div>

                    <div className={ styles.center }>
                         { characters.length > 0 && (
                              <>
                                   <ul>
                                        { characters.map((character) => (
                                             <li key={ character.id }>{ character.name }<img style={ { 'width': '500px' } } src={ 'http://127.0.0.1:8000/media/' + character.header_image } /><br />{ character.description }</li>
                                        )) }
                                   </ul>
                                   <div></div>
                              </>
                         ) }
                    </div>

               </main>
          </>
     );
}

export default Characters;
