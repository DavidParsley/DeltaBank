import { createContext, useContext, useEffect, useState } from "react";
import { toast } from "react-toastify";
import { UserContext } from "./UserContext";
import { useNavigate } from "react-router-dom";

export const LoanContext = createContext();

export const LoanProvider = ({ children }) => {

    const navigate = useNavigate();
    const { authToken } = useContext(UserContext);
    const [loans, setLoans] = useState([]);
    const [onChange, setOnChange] = useState(true);

  
// FETCH LOANS
    useEffect(() => {
      if (authToken) {
        fetch("http://127.0.0.1:5000/loans", {
          method: "GET",
          headers: {
            "Content-type": "application/json",
            Authorization: `Bearer ${authToken}`,
          },
        })
          .then((response) => response.json())
          .then((response) => {
            setLoans(response);
          })
          .catch((error) => {
            console.error("Error fetching loans:", error);
          });
      }
    }, [authToken, onChange]);
  

// ADD LOAN
const addLoan = (amount, interest_rate, loan_status, start_date, due_date, user_id) => {
    toast.loading("Processing... ");
    fetch("http://127.0.0.1:5000/loan", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
         Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify({
        amount,
        interest_rate,
        loan_status,
        start_date,
        due_date,
        user_id,
      }),
    })
      .then((resp) => resp.json())
      .then((response) => {
        console.log(response);

        if (response.success) {
          toast.dismiss();
          toast.success(response.success);
          navigate("/");
        } else if (response.error) {
          toast.dismiss();
          toast.error(response.error);
        } else {
          toast.dismiss();
          toast.error("Failed to add");
        }
      });
  };


  // UPDATE LOAN
  const updateLoan = (id, updated_amount, updated_interest_rate, updated_loan_status, updated_due_date) => {
    
    fetch(`http://127.0.0.1:5000/loan/${id}`, {
      method: "PATCH",
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify({
        amount: updated_amount,
        interest_rate: updated_interest_rate,
        loan_status: updated_loan_status,
        due_date: updated_due_date,
      }),
    })
      .then((resp) => resp.json())
      .then((response) => {
        if (response.success) {
          toast.success("Loan Updated ");
          navigate("/");
          setOnChange(!onChange)
        } else if (response.error) {
          toast.error("Loan Not Updated ");
        } else {
          alert("Failed to update");
        }
      })
      .catch((error) => console.error("Error updating entry:", error));
    console.log("Updating entry");
  };



    return <LoanContext.Provider value={data}>{children}</LoanContext.Provider>;
};    