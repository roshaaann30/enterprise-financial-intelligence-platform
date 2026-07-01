import Sidebar from "./Sidebar";

interface LayoutProps {
  children: React.ReactNode;
}

const SIDEBAR_WIDTH = 280;

export default function Layout({
  children,
}: LayoutProps) {
  return (
    <div
      style={{
        background: "#0B1020",
        minHeight: "100vh",
      }}
    >
      <Sidebar />

      <main
        style={{
          marginLeft: `${SIDEBAR_WIDTH}px`,
          width: `calc(100% - ${SIDEBAR_WIDTH}px)`,
          minHeight: "100vh",
          padding: "32px",
          boxSizing: "border-box",
          overflowX: "hidden",
          color: "white",
        }}
      >
        {children}
      </main>
    </div>
  );
}