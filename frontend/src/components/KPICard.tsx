type KPIProps = {

  title: string;

  value: number;

};

export default function KPICard({

  title,

  value,

}: KPIProps) {

  return (

    <div
      style={{

        border: "1px solid #444",

        borderRadius: "10px",

        padding: "20px",

        width: "220px",

        textAlign: "center",

        backgroundColor: "#161b22",

        boxShadow: "0px 4px 12px rgba(0,0,0,0.3)",

      }}
    >

      <h3>{title}</h3>

      <h1>{value}</h1>

    </div>

  );

}