import { React, useContext } from "react";
import logo from "../assets/card.png";
import { Link } from "react-router-dom";
import { LoanContext } from "../context/LoanContext";
import { UserContext } from "../context/UserContext";

export default function Home() {
  const { loans } = useContext(LoanContext);
  const { current_user, current_admin, logout } = useContext(UserContext);

  return (
    <div className="home-page">
      {/* Display this when no user is logged in */}
      {!current_user && !current_admin ? (
        <div>
          <div className="home-container">
            <div className="text-section">
              <h1 className="Home-h1 font-semibold text-gray-900 tracking-tight mb-4">
                Welcome to Delta Bank
              </h1>
              <p className="home-slogan text-lg text-gray-600 mb-6">
                We offer a secure, user-friendly platform that combines trust,
                simplicity, and innovation. Users and admins have full control
                over financial data and loans. Designed for efficiency, our
                system makes managing finances effortless while ensuring
                security and growth.
              </p>
            </div>
            <img src={logo} alt="Delta Bank Logo" className="heroImage" />
          </div>
          <div className="button-container flex space-x-4 justify-center mt-8">
            <Link to={"/register"}>
              <button className="registerbutton bg-a66cff text-white py-2 px-6 rounded-lg">
                Register
              </button>
            </Link>
            <Link to={"/login"}>
              <button className="registerbutton bg-gray-800 text-white py-2 px-6 rounded-lg">
                Login
              </button>
            </Link>
          </div>
        </div>
      ) : (
        // If the user is logged in
        <div>
          {/* For normal users */}
          {current_user && !current_admin ? (
            <div className="mt-16">
              <div className="welcome-container bg-white p-6 rounded-xl shadow-lg max-w-4xl mx-auto mb-8">
                <div className="flex items-center gap-4">
                  {" "}
                  {/* Use gap for spacing */}
                  <h1 className="text-3xl font-semibold text-gray-900 hover:text-[#a66cff]">
                    Welcome {current_user?.first_name} !
                  </h1>
                  {/* SVG Icon placed after the first name */}
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="30px" // You can adjust the size as per your design
                    viewBox="0 -960 960 960"
                    width="3px"
                    fill="green"
                    className="welcome-icon"
                  >
                    <path d="M441-120v-86q-53-12-91.5-46T293-348l74-30q15 48 44.5 73t77.5 25q41 0 69.5-18.5T587-356q0-35-22-55.5T463-458q-86-27-118-64.5T313-614q0-65 42-101t86-41v-84h80v84q50 8 82.5 36.5T651-650l-74 32q-12-32-34-48t-60-16q-44 0-67 19.5T393-614q0 33 30 52t104 40q69 20 104.5 63.5T667-358q0 71-42 108t-104 46v84h-80Z" />
                  </svg>
                </div>

                <p className="text-lg text-gray-600">
                  You have {loans && loans.length} loan(s).
                </p>
              </div>
              <div>
                {loans && loans.length < 1 && (
                  <div className="text-center text-black">
                    You don't have any loans
                    <button
                      onClick={logout}
                      className="text-a66cff bg-gray-900  border border-a66cff hover:bg-a66cff transition-colors duration-300 px-4 py-2 rounded mt-2"
                    >
                      Log Out?
                    </button>
                  </div>
                )}
                {/* Container for loan cards */}
                <div className="loan-cards-container mt-8 bg-purple-600 p-8 rounded-3xl">
                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    {loans &&
                      loans.map((loan) => (
                        <div
                          className="flex items-center justify-center p-4"
                          key={loan.id}
                        >
                          <div className="loan-card bg-gray-900 rounded-xl shadow-md transition-all transform hover:scale-105 hover:shadow-2xl">
                            <div className="relative rounded-t-xl overflow-hidden">
                              <img
                                src={logo}
                                alt="Loan"
                                className="w-full h-52 object-cover rounded-t-xl"
                              />
                            </div>

                            <div className="p-6 space-y-6 text-gray-800">
                              {/* Top Section: Dates */}
                              <div className="flex justify-between">
                                <div>
                                  <span className="text-sm text-[#d0f500d7]">
                                    Start Date:
                                  </span>
                                  <h3 className="font-semibold text-gray-300">
                                    {new Date(
                                      loan.start_date
                                    ).toLocaleDateString()}
                                  </h3>
                                </div>
                                <div>
                                  <span className="text-sm text-[#a66cff]">
                                    Due Date:
                                  </span>
                                  <h3 className="font-semibold text-gray-300">
                                    {new Date(
                                      loan.due_date
                                    ).toLocaleDateString()}
                                  </h3>
                                </div>
                              </div>

                              {/* Middle Section: Loan Details */}
                              <div className="flex justify-between">
                                <div>
                                  <span className="text-sm text-[#d0f500d7]">
                                    Amount:
                                  </span>
                                  <h3 className="font-semibold text-[#d0f500d7]">
                                    ${loan.amount}
                                  </h3>
                                </div>
                                <div>
                                  <span className="text-sm text-[#a66cff]">
                                    Interest Rate:
                                  </span>
                                  <h3 className="font-semibold text-[#a66cff]">
                                    {loan.interest_rate}%
                                  </h3>
                                </div>
                              </div>

                              {/* Bottom Section: Loan Status */}
                              <div className="mt-4 text-center">
                                <span
                                  className={`${
                                    loan.loan_status === "Paid"
                                      ? "text-green-600"
                                      : "text-red-500"
                                  } text-lg font-semibold hover:text-white`}
                                >
                                  {loan.loan_status}
                                </span>
                              </div>
                            </div>
                          </div>
                        </div>
                      ))}
                  </div>
                </div>
              </div>
            </div>
          ) : null}

          {/* For admin users */}
          {current_admin && !current_user ? (
            <div className="mt-16">
              <div className="welcome-container bg-white p-6 rounded-xl shadow-lg max-w-lg mx-auto mb-8 text-center">
                <div className="flex justify-center gap-4">
                  {" "}
                  {/* Use gap for spacing */}
                  <h1 className="text-3xl font-semibold text-gray-900 hover:text-[#a66cff]">
                    Welcome {current_admin?.first_name} !
                  </h1>
                  {/* SVG Icon placed after the first name */}
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    height="30px" // You can adjust the size as per your design
                    viewBox="0 -960 960 960"
                    width="3px"
                    fill="green"
                    className="welcome-icon"
                  >
                    <path d="M441-120v-86q-53-12-91.5-46T293-348l74-30q15 48 44.5 73t77.5 25q41 0 69.5-18.5T587-356q0-35-22-55.5T463-458q-86-27-118-64.5T313-614q0-65 42-101t86-41v-84h80v84q50 8 82.5 36.5T651-650l-74 32q-12-32-34-48t-60-16q-44 0-67 19.5T393-614q0 33 30 52t104 40q69 20 104.5 63.5T667-358q0 71-42 108t-104 46v84h-80Z" />
                  </svg>
                </div>

                <p className="text-lg text-gray-600">
                  Total loans in the database : {loans && loans.length} loan(s).
                </p>
              </div>
              <div>
                {loans && loans.length < 1 && (
                  <div className="text-center text-white">
                    There are no loans
                    <button
                      onClick={logout}
                      className="text-a66cff hover:text-white border border-a66cff hover:bg-a66cff transition-colors duration-300 px-4 py-2 rounded mt-2"
                    >
                      Log Out?
                    </button>
                  </div>
                )}
                {/* Container for loan cards */}
                <div className="loan-cards-container mt-8 bg-purple-600 p-8 rounded-3xl">
                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    {loans &&
                      loans.map((loan) => (
                        <div
                          className="flex items-center justify-center p-4"
                          key={loan.id}
                        >
                          <div className="loan-card bg-gray-900 rounded-xl shadow-md transition-all transform hover:scale-105 hover:shadow-2xl">
                            <div className="relative rounded-t-xl overflow-hidden">
                              <img
                                src={logo}
                                alt="Loan"
                                className="w-full h-52 object-cover rounded-t-xl"
                              />
                            </div>

                            <div className="p-6 space-y-6 text-gray-800">
                              {/* Top Section: Dates */}
                              <div className="flex justify-between">
                                <div>
                                  <span className="text-sm text-[#d0f500d7]">
                                    Start Date:
                                  </span>
                                  <h3 className="font-semibold text-gray-300">
                                    {new Date(
                                      loan.start_date
                                    ).toLocaleDateString()}
                                  </h3>
                                </div>
                                <div>
                                  <span className="text-sm text-[#a66cff]">
                                    Due Date:
                                  </span>
                                  <h3 className="font-semibold text-gray-300">
                                    {new Date(
                                      loan.due_date
                                    ).toLocaleDateString()}
                                  </h3>
                                </div>
                              </div>

                              {/* Middle Section: Loan Details */}
                              <div className="flex justify-between">
                                <div>
                                  <span className="text-sm text-[#d0f500d7]">
                                    Amount:
                                  </span>
                                  <h3 className="font-semibold text-[#d0f500d7]">
                                    ${loan.amount}
                                  </h3>
                                </div>
                                <div>
                                  <span className="text-sm text-[#a66cff]">
                                    Interest Rate:
                                  </span>
                                  <h3 className="font-semibold text-[#a66cff]">
                                    {loan.interest_rate}%
                                  </h3>
                                </div>
                              </div>

                              {/* Bottom Section: Loan Status */}
                              <div className="mt-4 flex justify-between items-center">
                                <span
                                  className={`${
                                    loan.loan_status === "Paid"
                                      ? "text-green-600"
                                      : "text-red-500"
                                  } text-sm font-semibold`}
                                >
                                  {loan.loan_status}
                                </span>
                                <button className="bg-a66cff text-black font-medium py-2 px-4 rounded-lg transition-colors bg-[#d0f500d7] hover:bg-indigo-700  hover:text-white">
                                  <Link to={`/singleloan/${loan.id}`}>View Details</Link>
                                </button>
                              </div>
                            </div>
                          </div>
                        </div>
                      ))}
                  </div>
                </div>
              </div>
            </div>
          ) : null}
        </div>
      )}
    </div>
  );
}
