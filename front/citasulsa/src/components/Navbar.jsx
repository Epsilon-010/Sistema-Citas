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
    {
      name: "Home",
      icon: <HomeIcon className="w-5 h-5" />,
      path: "/Bienvda",
    },
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
    <aside className="w-64 bg-[#1e3a8a] text-white flex flex-col fixed h-screen">
      <div className="flex items-center justify-center bg-[#60a5fa] py-4">
        <img src="/logo.png" alt="La Salle Oaxaca" className="h-12" />
      </div>
      <nav className="flex flex-col mt-6 space-y-4 pl-6">
        {menuItems.map((item) => (
          <Link
            key={item.name}
            to={item.path}
            className={`flex items-center gap-3 py-2 hover:opacity-90 transition ${
              location.pathname === item.path
                ? "font-semibold text-[#60a5fa]"
                : ""
            }`}
          >
            {item.icon}
            {item.name}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
