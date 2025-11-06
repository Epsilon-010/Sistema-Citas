import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Login from "./components/login";
import Bienvda from "./components/Bienvda";
import Agregar from "./components/Agregar";
import Consultar from "./components/Consultar";
import Reagendar from "./components/Reagendar";
import Calendario from "./components/Calendario";
import Navbar from "./components/Navbar";
import Topbar from "./components/TopBar";

const App = () => {
  const [isOpen, setIsOpen] = useState(false);
  const toggleNavbar = () => setIsOpen(!isOpen);
  const [visitantes, setVisitantes] = useState([]);

  // 🔹 Estructura del layout con navbar lateral y topbar superior
  const PageLayout = ({ children }) => (
    <div className="flex">
      {/* Navbar lateral fija */}
      <Navbar isOpen={isOpen} toggleNavbar={toggleNavbar} />

      {/* Contenido principal */}
      <div className="flex-1 md:ml-64 bg-[#f9fafb] min-h-screen pt-14">
        <Topbar toggleNavbar={toggleNavbar} />
        <div className="p-8">{children}</div>
      </div>
    </div>
  );

  return (
    <Router>
      <Routes>
        {/* Página de login sin navbar */}
        <Route path="/" element={<Login />} />

        {/* Páginas con navbar y topbar */}
        <Route
          path="/bienvda"
          element={
            <PageLayout>
              <Bienvda />
            </PageLayout>
          }
        />
        <Route
          path="/agregar"
          element={
            <PageLayout>
              <Agregar visitantes={visitantes} setVisitantes={setVisitantes} />
            </PageLayout>
          }
        />
        <Route
          path="/consultar"
          element={
            <PageLayout>
              <Consultar
                visitantes={visitantes}
                setVisitantes={setVisitantes}
              />
            </PageLayout>
          }
        />
        <Route
          path="/reagendar"
          element={
            <PageLayout>
              <Reagendar />
            </PageLayout>
          }
        />
        <Route
          path="/calendario"
          element={
            <PageLayout>
              <Calendario />
            </PageLayout>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;
