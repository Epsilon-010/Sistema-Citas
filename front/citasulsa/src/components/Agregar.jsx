import { useState } from "react";
import Navbar from "./Navbar"; // tu componente de navegación

export default function Agregar() {
  const [mostrarNavbar, setMostrarNavbar] = useState(true);

  const toggleNavbar = () => {
    setMostrarNavbar(!mostrarNavbar);
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Navbar lateral */}
      {mostrarNavbar && <div className="w-64"></div>}

      {/* Contenido principal */}
      <div className="flex flex-col flex-1">
        {/* Barra superior */}
        <div className="bg-blue-900 text-white px-6 py-4 flex items-center justify-between shadow-md">
          <button onClick={toggleNavbar} className="text-2xl font-bold">
            ☰
          </button>
          <h1 className="text-lg font-semibold">Registro de visita</h1>
        </div>

        {/* Formulario */}
        <div className="p-8 space-y-8">
          {/* Datos personales */}
          <div className="bg-white p-6 rounded-lg shadow-md border border-blue-300">
            <h2 className="text-xl font-semibold mb-4 text-blue-900">
              Datos personales de la visita
            </h2>
            <div className="grid grid-cols-2 gap-6">
              <input
                type="text"
                placeholder="Nombre completo"
                className="input"
              />
              <select className="input">
                <option>Género</option>
                <option>Femenino</option>
                <option>Masculino</option>
                <option>Otro</option>
              </select>
              <input
                type="date"
                placeholder="Fecha de nacimiento"
                className="input"
              />
              <input type="text" placeholder="INE" className="input" />
              <input
                type="email"
                placeholder="Correo electrónico"
                className="input"
              />
              <input
                type="tel"
                placeholder="Número de celular"
                className="input"
              />
            </div>
          </div>

          {/* Datos de la cita */}
          <div className="bg-white p-6 rounded-lg shadow-md border border-blue-300">
            <h2 className="text-xl font-semibold mb-4 text-blue-900">
              Datos de la cita
            </h2>
            <div className="grid grid-cols-2 gap-6">
              <input type="date" placeholder="Fecha" className="input" />
              <input type="time" placeholder="Hora" className="input" />
              <input
                type="text"
                placeholder="Área o departamento visitado"
                className="input"
              />
              <input
                type="text"
                placeholder="Persona a quien se visita"
                className="input"
              />
            </div>
          </div>

          {/* Medio de ingreso */}
          <div className="bg-white p-6 rounded-lg shadow-md border border-blue-300">
            <h2 className="text-xl font-semibold mb-4 text-blue-900">
              Medio de ingreso
            </h2>
            <div className="space-y-4">
              <div className="flex items-center gap-4">
                <label className="flex items-center gap-2">
                  <input type="radio" name="ingreso" value="pie" />A pie
                </label>
                <label className="flex items-center gap-2">
                  <input type="radio" name="ingreso" value="vehiculo" />
                  En vehículo
                </label>
              </div>

              {/* Datos del vehículo */}
              <div className="grid grid-cols-4 gap-4">
                <input type="text" placeholder="Marca" className="input" />
                <input type="text" placeholder="Modelo" className="input" />
                <input type="text" placeholder="Color" className="input" />
                <input type="text" placeholder="Placas" className="input" />
              </div>
            </div>
          </div>

          {/* Botón registrar */}
          <div className="flex justify-end">
            <button className="bg-blue-900 text-white px-6 py-2 rounded-md shadow hover:bg-blue-800 transition">
              Registrar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
