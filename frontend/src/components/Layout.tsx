import Sidebar from "./Sidebar";

export default function Layout({

  children,

}: any) {

  return (

    <div>

      <Sidebar />

      <div
        style={{
          marginLeft: "250px",
          padding: "20px",
        }}
      >

        {children}

      </div>

    </div>

  );

}