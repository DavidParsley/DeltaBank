import { useContext, useState } from "react";
import { Link } from "react-router-dom";
import { UserContext } from "../context/UserContext";

export default function Navbar() {
  const { logout, current_user, current_admin } = useContext(UserContext);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  return (
    <nav className="Navbar fixed top-0 left-0 w-full z-50 bg-white shadow-xl rounded-b-3xl">
      <div className="max-w-screen-xl flex items-center justify-between mx-auto p-4">
        <Link to="/" className="Navbar-logo flex items-center space-x-3 text-3xl font-bold">
          <span className="text-black hover:text-purple-600">Delta Bank</span>
          <svg xmlns="http://www.w3.org/2000/svg" height="31px" width="31px" viewBox="0 -960 960 960" fill="black">
            <path d="M200-280v-280h80v280h-80Zm240 0v-280h80v280h-80ZM80-120v-80h800v80H80Zm600-160v-280h80v280h-80ZM80-640v-80l400-200 400 200v80H80Zm178-80h444-444Zm0 0h444L480-830 258-720Z" />
          </svg>
        </Link>

        {current_user || current_admin ? (
          <div className="flex items-center space-x-4">
        {/* <Link to="/loans" className="block px-4 py-2 text-sm hover:text-green-600">Profile</Link> */}

            <button
              type="button"
              className="flex items-center justify-center w-13 h-13 bg-white"
              onClick={() => setDropdownOpen(!dropdownOpen)}
            >
              <span className="sr-only">Open user menu</span>
              <img
                className="w-13 h-13 rounded-full border-2 border-[#d0f500d7]  hover:bg-red-400 "
                src={`https://ui-avatars.com/api/?name=${encodeURIComponent(current_user?.first_name || current_admin?.first_name)}+${encodeURIComponent(current_user?.last_name || current_admin?.last_name)}&background=random`}
                alt="user photo"
              />
            </button>

            {dropdownOpen && (
              <div className="absolute top-full right-0 mt-2 w-48 bg-white shadow-lg rounded-lg p-3 border border-gray-200 text-center">
                <div className="text-sm">
                  <span className="block text-black font-medium ">
                   
                    {current_user?.first_name || current_admin?.first_name}
                    {" "}
                    {current_user?.last_name || current_admin?.last_name}
                  </span>
                  <span className="block text-gray-500 truncate dark:text-gray-400">
                    {current_user?.email || current_admin?.email}
                  </span>
                </div>
                <ul className="mt-2">
                  {current_user && (
                    <>
                      {/* <li><Link to="/profile" className="block px-4 py-2 text-sm hover:text-purple-600">Profile</Link></li> */}
                      <li><Link to="/" className="block px-4 py-2 text-sm hover:bg-purple-100">Home</Link></li>
                      <li><Link to="/profile" className="block px-4 py-2 text-sm hover:bg-purple-100">Profile</Link></li>
                      <li><Link to="/" onClick={logout} className="block px-4 py-2 text-sm hover:text-red-600">Sign out</Link></li>
                    </>
                  )}

                  {current_admin && (
                    <>
                      <li><Link to="/" className="block px-4 py-2 text-sm hover:bg-purple-100">Home</Link></li>
                      <li><Link to="/profile" className="block px-4 py-2 text-sm hover:bg-purple-100">Profile</Link></li>
                      <li><Link to="/addloan" className="block px-4 py-2 text-sm hover:bg-purple-100">Grant Loan</Link></li>
                      <li><Link to="/accounts" className="block px-4 py-2 text-sm hover:bg-purple-100">Accounts</Link></li>
                      <li><Link to="/" onClick={logout} className="block px-4 py-2 text-sm  hover:text-red-600">Sign out</Link></li>
                    </>
                  )}
                </ul>
              </div>
            )}
          </div>
        ) : (
          <div className="Navbar-links flex-grow flex justify-center space-x-6">
            <Link to="/" className="text-gray-700 text-lg hover:text-purple-600">Home</Link>
            <Link to="/about" className="text-gray-700 text-lg hover:text-purple-600">About</Link>
          </div>
        )}
      </div>
    </nav>
  );
}
