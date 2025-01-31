import { React, useContext, useState } from "react";
import { LoanContext } from "../context/LoanContext";
import { UserContext } from "../context/UserContext";

export default function AddLoan() {
  const { addLoan } = useContext(LoanContext);
  const { users } = useContext(UserContext);

  const [amount, setAmount] = useState("");
  const [interest_rate, setInterestRate] = useState("");
  const [loan_status, setLoanStatus] = useState("");
  const [start_date, setStartDate] = useState("");
  const [due_date, setDueDate] = useState("");
  const [user_id, setUserId] = useState(0);

  function handleSubmit(e) {
    e.preventDefault();
    addLoan(amount, interest_rate, loan_status, start_date, due_date, user_id);
  }

  return (
    <div className="Register-form font-[sans-serif] max-w-4xl flex items-center mx-auto p-4 mt-18">
      <div className="grid md:grid-cols-3 gap-6 items-center shadow-[0_2px_10px_-3px_rgba(6,81,237,0.3)] rounded-xl ">
        <div className="Register-form-text max-md:order-1 flex flex-col justify-center md:space-y-16 space-y-8 max-md:mt-16 min-h-full b lg:px-8 px-4 py-4">
          <div>
            <h4 className="text-lg">Create a loan</h4>
            <p className="text-[14px] mt-3 leading-relaxed">
              Welcome to our loan creation page! Get started by creating a loan.
            </p>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="md:col-span-2 w-full py-6 px-6 sm:px-16 max-md:max-w-xl mx-auto">
          <div className="mb-6">
            <h3 className="text-gray-800 text-xl font-bold">Create a Loan</h3>
          </div>

          <div className="space-y-6">
            <div>
              <label className="text-gray-600 text-sm mb-2 block">Amount</label>
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                required
                className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                placeholder="Enter amount"
              />
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Interest Rate</label>
              <input
                type="number"
                value={interest_rate}
                onChange={(e) => setInterestRate(e.target.value)}
                required
                className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                placeholder="Enter interest rate"
              />
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Loan Status</label>
              <input
                type="text"
                value={loan_status}
                onChange={(e) => setLoanStatus(e.target.value)}
                required
                className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                placeholder="Enter loan status"
              />
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Start Date</label>
              <input
                type="date"
                value={start_date}
                onChange={(e) => setStartDate(e.target.value)}
                required
                className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                min={new Date().toISOString().split('T')[0]} // Prevent past dates
              />
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Due Date</label>
              <input
                type="date"
                value={due_date}
                onChange={(e) => setDueDate(e.target.value)}
                required
                className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                min={new Date().toISOString().split('T')[0]}
             />
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Account</label>
              <select
                value={user_id}
                onChange={(e) => setUserId(e.target.value)}
                className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
              >
                <option value={0}>Select Account</option>
                {users.map((user) => (
                  <option key={user.id} value={user.id}>
                    {user.first_name} {user.last_name} 
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="mt-8">
            <button type="submit" className="w-full py-2.5 px-4 tracking-wider text-sm rounded-md text-black bg-[#d0f500d7] hover:bg-purple-700 focus:outline-none">
              Assign loan
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
