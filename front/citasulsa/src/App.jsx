import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./components/login";
import Bienvda from "./components/Bienvda";
import Agregar from "./components/Agregar";
import Navbar from "./components/Navbar";
import Consultar from "./components/Consultar";
import Reagendar from "./components/Reagendar";
import Calendario from "./components/Calendario";
// Si después agregas más pantallas:
// import Consultar from "./components/Consultar";
// import Reagendar from "./components/Reagendar";
// import Calendario from "./components/Calendario";

const App = () => {
  return (
    <Router>
      <Routes>
        {/* Página de login sin navbar */}
        <Route path="/" element={<Login />} />

        {/* Pantalla de bienvenida */}
        <Route
          path="/bienvenida"
          element={
            <div className="flex items-center justify-center min-h-screen bg-[#f9fafb] px-10">
              <div className="bg-white shadow-2xl rounded-3xl p-12 w-full max-w-[1200px] flex justify-center">
                <Bienvda />
              </div>
            </div>
          }
        />
        <Route
          path="/Agregar"
          element={
            <div className="flex">
              <Navbar />
              <div className="flex-1 ml-64 p-10 bg-[#f9fafb] min-h-screen">
                <Agregar />
              </div>
            </div>
          }
        />
        <Route
          path="/Consultar"
          element={
            <div className="flex">
              <Navbar />
              <div className="flex-1 ml-64 p-10 bg-[#f9fafb] min-h-screen">
                <Consultar />
              </div>
            </div>
          }
        />
        <Route
          path="/Reagendar"
          element={
            <div className="flex">
              <Navbar />
              <div className="flex-1 ml-64 p-10 bg-[#f9fafb] min-h-screen">
                <Reagendar />
              </div>
            </div>
          }
        />
        <Route
          path="/Calendario"
          element={
            <div className="flex">
              <Navbar />
              <div className="flex-1 ml-64 p-10 bg-[#f9fafb] min-h-screen">
                <Calendario />
              </div>
            </div>
          }
        />
        <Route
          path="/Bienvda"
          element={
            <div className="flex">
              <Navbar />
              <div className="flex-1 ml-64 p-10 bg-[#f9fafb] min-h-screen">
                <Bienvda />
              </div>
            </div>
          }
        />

        {/* Otras pantallas */}
        <Route path="/agregar" element={<Agregar />} />
        {/* Ejemplo si luego agregas más: */}
        {/* <Route path="/consultar" element={<Consultar />} /> */}
        {/* <Route path="/reagendar" element={<Reagendar />} /> */}
        {/* <Route path="/calendario" element={<Calendario />} /> */}
      </Routes>
    </Router>
  );
};

export default App;
