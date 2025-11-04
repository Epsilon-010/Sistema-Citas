import { Link, useLocation } from "react-router-dom";
import {
  PlusIcon,
  BookOpenIcon,
  PencilIcon,
  CalendarIcon,
  HomeIcon,
} from "@heroicons/react/24/outline";

export default function Navbar() {
  const location = useLocation();

  const menuItems = [
    { name: "Home", icon: <HomeIcon className="w-5 h-5" />, path: "/Bienvda" },
    {
      name: "Agregar",
      icon: <PlusIcon className="w-5 h-5" />,
      path: "/agregar",
    },
    {
      name: "Consultar",
      icon: <BookOpenIcon className="w-5 h-5" />,
      path: "/consultar",
    },
    {
      name: "Reagendar",
      icon: <PencilIcon className="w-5 h-5" />,
      path: "/reagendar",
    },
    {
      name: "Calendario",
      icon: <CalendarIcon className="w-5 h-5" />,
      path: "/calendario",
    },
  ];

  return (
    <aside className="w-64 bg-[#1e3a8a] text-white flex flex-col fixed h-screen shadow-lg font-sans">
      {/* Encabezado con logo */}

      <img src="/logo.jpg" alt="La Salle Oaxaca" className="h-24 full-shadow" />

      {/* Menú */}
      <nav className="flex flex-col mt-8 space-y-3 pl-8 pr-4">
        {menuItems.map((item) => (
          <Link
            key={item.name}
            to={item.path}
            className={`flex items-center gap-4 py-3 px-3 rounded-xl transition-all duration-200 ${
              location.pathname === item.path
                ? "bg-[#182d83] text-gray-100"
                : "hover:bg-[#182d83] hover:text-gray-100"
            }`}
          >
            {item.icon}
            <span className="text-md font-medium tracking-wide">
              {item.name}
            </span>
          </Link>
        ))}
      </nav>
    </aside>
  );
}
