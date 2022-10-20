import React, { useState, useEffect } from "react";

export default ({ data }) => {
  return (
    <main>
      <h1>Welcome to Next.js</h1>
      <h1>{data}</h1>
    </main>
  );
};

export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`http://127.0.0.1:5000`);
  console.log(res);
  const data = await res.json();
  console.log(`data ------------------------ ${data}`);

  // Pass data to the page via props
  return { props: { data } };
}
