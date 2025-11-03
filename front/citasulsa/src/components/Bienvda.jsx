import {
  UserCircleIcon,
  PlusIcon,
  BookOpenIcon,
  PencilIcon,
  CalendarIcon,
} from "@heroicons/react/24/outline";
import { useNavigate } from "react-router-dom";

export default function Bienvenida() {
  const navigate = useNavigate();
  const fecha = new Date().toLocaleDateString("es-MX", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });

  return (
    <main className="flex-1 p-12 bg-[#f9fafb] rounded-tl-2xl shadow-inner min-h-screen flex flex-col items-center justify-center font-[Mitr]">
      {/* Tarjeta de bienvenida */}
      <div className="flex flex-col md:flex-row items-center gap-10 bg-white shadow-2xl rounded-3xl p-12 w-full max-w-4xl transition-transform hover:scale-[1.01] duration-200">
        {/* Icono del usuario */}
        <UserCircleIcon className="w-36 h-36 text-[#1e3a8a]" />

        {/* Texto de bienvenida */}
        <div className="text-center md:text-left">
          <h2 className="text-3xl mb-2">
            ¡Bienvenido de nuevo <span className="text-[#1e3a8a]">USER01</span>!
          </h2>
          <p className="text-base text-gray-600 mb-1">{fecha}</p>
          <p className="text-lg font-medium">
            Tipo de usuario:{" "}
            <span className="text-[#1e3a8a]">Administrador universitario</span>
          </p>
        </div>
      </div>

      {/* Cuadros de acción */}
      <div className="mt-20 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 w-full max-w-6xl">
        {/* Agregar Cita */}
        <div
          onClick={() => navigate("/agregar")}
          className="bg-[#e0e7ff] hover:bg-[#c7d2fe] shadow-md rounded-2xl p-6 text-center cursor-pointer hover:scale-105 transition-all duration-300"
        >
          <PlusIcon className="w-10 h-10 mx-auto text-[#1e3a8a]" />
          <p className="mt-2 font-semibold text-[#1e3a8a]">Agregar Cita</p>
        </div>

        {/* Consultar Registros */}
        <div
          onClick={() => navigate("/consultar")}
          className="bg-[#e0e7ff] hover:bg-[#c7d2fe] shadow-md rounded-2xl p-6 text-center cursor-pointer hover:scale-105 transition-all duration-300"
        >
          <BookOpenIcon className="w-10 h-10 mx-auto text-[#1e3a8a]" />
          <p className="mt-2 font-semibold text-[#1e3a8a]">
            Consultar Registros
          </p>
        </div>

        {/* Reagendar */}
        <div
          onClick={() => navigate("/reagendar")}
          className="bg-[#e0e7ff] hover:bg-[#c7d2fe] shadow-md rounded-2xl p-6 text-center cursor-pointer hover:scale-105 transition-all duration-300"
        >
          <PencilIcon className="w-10 h-10 mx-auto text-[#1e3a8a]" />
          <p className="mt-2 font-semibold text-[#1e3a8a]">Reagendar</p>
        </div>

        {/* Calendario */}
        <div
          onClick={() => navigate("/calendario")}
          className="bg-[#e0e7ff] hover:bg-[#c7d2fe] shadow-md rounded-2xl p-6 text-center cursor-pointer hover:scale-105 transition-all duration-300"
        >
          <CalendarIcon className="w-10 h-10 mx-auto text-[#1e3a8a]" />
          <p className="mt-2 font-semibold text-[#1e3a8a]">Calendario</p>
        </div>
      </div>
    </main>
  );
}
