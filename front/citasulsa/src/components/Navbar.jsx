import { Link, useLocation } from "react-router-dom";
import {
  PlusIcon,
  BookOpenIcon,
  PencilIcon,
  CalendarIcon,
  HomeModernIcon,
} from "@heroicons/react/24/outline";
import { HomeIcon } from "@heroicons/react/20/solid";

export default function Navbar() {
  const location = useLocation();

  const menuItems = [
    {
      name: "Home",
      icon: <HomeIcon className="w-5 h-5 font-[Mitr]" />,
      path: "/bienvda",
    },
    {
      name: "Agregar",
      icon: <PlusIcon className="w-5 h-5 font-[Mitr]" />,
      path: "/agregar",
    },
    {
      name: "Consultar",
      icon: <BookOpenIcon className="w-5 h-5 font-[Mitr]" />,
      path: "/consultar",
    },
  ];

  return (
    <aside className="w-64 bg-[#1e3a8a] text-white flex flex-col fixed h-screen shadow-lg">
      <div className="flex flex-col items-center justify-center bg-white py-6">
        <img src="/logo.jpg" alt="Logo La Salle" className="h-24" />
      </div>

      <nav className="flex flex-col mt-6 space-y-3 pl-6 pr-4">
        {menuItems.map((item) => (
          <Link
            key={item.name}
            to={item.path}
            className={`flex items-center gap-3 py-3 px-3 rounded-xl transition-all duration-200 ${
              location.pathname === item.path
                ? "bg-white text-[#1e3a8a] font-semibold"
                : "hover:bg-[#243c96]"
            }`}
          >
            {item.icon}
            <span className="text-md">{item.name}</span>
          </Link>
        ))}
      </nav>
    </aside>
  );
}
