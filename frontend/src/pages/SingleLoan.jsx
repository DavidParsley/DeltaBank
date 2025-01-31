import React, { useState, useContext, useEffect } from "react";
import { LoanContext } from "../context/LoanContext";
import { useParams } from "react-router-dom";
import { UserContext } from "../context/UserContext";

export default function SingleLoan() {
  const { current_admin } = useContext(UserContext);
  const { loans, updateLoan, deleteLoan } = useContext(LoanContext);
  const { id } = useParams();
  const loan = loans && loans.find((loan) => loan.id == id);
  const [amount, setAmount] = useState("");
  const [interest_rate, setInterestRate] = useState("");
  const [loan_status, setLoanStatus] = useState("");
  const [due_date, setDueDate] = useState("");

  useEffect(() => {
    if (loan) {
      setAmount(loan.amount);
      setInterestRate(loan.interest_rate);
      setLoanStatus(loan.loan_status);

      const formattedDueDate = loan.due_date ? new Date(loan.due_date).toISOString().split('T')[0] : '';
      setDueDate(formattedDueDate);
    }
  }, [loan]);

  function handleSubmit(e){
    e.preventDefault();
    updateLoan(loan.id, amount, interest_rate, loan_status, due_date);

  }

  function handleDelete(e){
    e.preventDefault()
    deleteLoan(loan.id); 

  }

 

  return (
    <div className="flex justify-center items-center space-x-8 p-8 mt-10">
      {/* Loan Card */}
      <div className="flex flex-col rounded-lg bg-slate-700 shadow-sm p-8 border border-slate-600 min-w-[320px]">
        <div className="pb-8 m-0 mb-8 text-center text-slate-100 border-b border-slate-600">
          <h2 className="text-sm uppercase font-semibold text-slate-300">
            Loan Details
          </h2>
          <h1 className="flex justify-center gap-1 mt-4 font-bold text-white text-6xl">
            <span className="text-3xl">$</span>
            {amount}
          </h1>
        </div>
        <div className="p-0">
          <ul className="flex flex-col gap-4">
            <li className="flex items-center gap-4">
              <h3 className="text-slate-300">
                Borrower:{" "}
                {loan && loan.user_id
                  ? `${loan.user_id["First Name"]} ${loan.user_id["Last Name"]}`
                  : "Loading..."}
              </h3>
            </li>
            <li className="flex items-center gap-4">
              <h3 className="text-slate-300">
                Interest Rate: {interest_rate}%
              </h3>
            </li>
            <li className="flex items-center gap-4">
              <h3 className="text-slate-300">Loan Status: {loan_status}</h3>
            </li>
            <li className="flex items-center gap-4">
              <h3 className="text-slate-300">Due Date: {due_date}</h3>
            </li>
          </ul>
        </div>
        <div className="p-0 mt-12">
          <button
            onClick={handleDelete} 
            className="min-w-32 w-full rounded-md bg-red-600 py-2 px-4 border border-transparent text-center text-sm text-white transition-all shadow-md hover:shadow-lg focus:bg-red-700 focus:shadow-none active:bg-red-800 hover:bg-red-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
          >
            Delete
          </button>
        </div>
      </div>

      {/* Update Form */}
      <div className="w-full max-w-md p-8 bg-slate-700 border border-slate-600 rounded-lg">
        <h2 className="text-2xl font-semibold text-white mb-6">
          Update Loan Details
        </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="flex items-center gap-4">
            <label htmlFor="amount" className="text-white">
              Amount ($)
            </label>
            <input
              type="number"
              id="amount"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              className="px-4 py-2 rounded-md border border-slate-500 bg-slate-800 text-white w-full"
            />
          </div>
          <div className="flex items-center gap-4">
            <label htmlFor="interest_rate" className="text-white">
              Interest Rate (%)
            </label>
            <input
              type="number"
              id="interest_rate"
              value={interest_rate}
              onChange={(e) => setInterestRate(e.target.value)}
              className="px-4 py-2 rounded-md border border-slate-500 bg-slate-800 text-white w-full"
            />
          </div>
          <div className="flex items-center gap-4">
            <label htmlFor="loan_status" className="text-white">
              Loan Status
            </label>
            <input
              type="text"
              id="loan_status"
              value={loan_status}
              onChange={(e) => setLoanStatus(e.target.value)}
              className="px-4 py-2 rounded-md border border-slate-500 bg-slate-800 text-white w-full"
            />
          </div>
          <div className="flex items-center gap-4">
            <label htmlFor="due_date" className="text-white">
              Due Date
            </label>
            <input
              type="date"
              id="due_date"
              value={due_date}
              onChange={(e) => setDueDate(e.target.value)}
              className="px-4 py-2 rounded-md border border-slate-500 bg-slate-800 text-white w-full"
            />
          </div>
          {!current_admin ? (
            <div>You must be an admin to update this loan.</div>
          ) : (
            <button
              type="submit"
              className="w-full bg-green-600 py-2 px-4 rounded-md text-white text-sm mt-6"
            >
              Update
            </button>
          )}
        </form>
      </div>
    </div>
  );
}
