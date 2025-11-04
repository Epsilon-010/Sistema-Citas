import { useEffect, useState } from "react";

export default function Consultar() {
  const [visitas, setVisitas] = useState([]);

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem("visitas")) || [];
    setVisitas(data);
  }, []);

  return (
    <div className="flex flex-col min-h-screen bg-[#f9fafb]">
      <div className="bg-[#1a237e] text-white p-4 flex justify-between items-center">
        <h1 className="text-lg font-semibold">Consultar visitas</h1>
      </div>

      <div className="p-8 overflow-x-auto">
        <table className="min-w-full bg-white border rounded-lg shadow text-sm">
          <thead className="bg-[#1a237e] text-white">
            <tr>
              <th className="px-4 py-2 border">Nombre</th>
              <th className="px-4 py-2 border">Género</th>
              <th className="px-4 py-2 border">Nacimiento</th>
              <th className="px-4 py-2 border">INE</th>
              <th className="px-4 py-2 border">Correo</th>
              <th className="px-4 py-2 border">Celular</th>
              <th className="px-4 py-2 border">Fecha cita</th>
              <th className="px-4 py-2 border">Hora</th>
              <th className="px-4 py-2 border">Área</th>
              <th className="px-4 py-2 border">Persona</th>
              <th className="px-4 py-2 border">Medio</th>
              <th className="px-4 py-2 border">Marca</th>
              <th className="px-4 py-2 border">Modelo</th>
              <th className="px-4 py-2 border">Color</th>
              <th className="px-4 py-2 border">Placas</th>
            </tr>
          </thead>
          <tbody>
            {visitas.length > 0 ? (
              visitas.map((v, i) => (
                <tr key={i} className="border-t hover:bg-gray-100">
                  <td className="px-4 py-2">{v.nombre}</td>
                  <td className="px-4 py-2">{v.genero}</td>
                  <td className="px-4 py-2">{v.fechaNacimiento}</td>
                  <td className="px-4 py-2">{v.ine}</td>
                  <td className="px-4 py-2">{v.correo}</td>
                  <td className="px-4 py-2">{v.celular}</td>
                  <td className="px-4 py-2">{v.fechaCita}</td>
                  <td className="px-4 py-2">{v.horaCita}</td>
                  <td className="px-4 py-2">{v.area}</td>
                  <td className="px-4 py-2">{v.persona}</td>
                  <td className="px-4 py-2">{v.medio}</td>
                  <td className="px-4 py-2">{v.marca}</td>
                  <td className="px-4 py-2">{v.modelo}</td>
                  <td className="px-4 py-2">{v.color}</td>
                  <td className="px-4 py-2">{v.placas}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="15" className="text-center py-4 text-gray-500">
                  No hay registros disponibles.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
