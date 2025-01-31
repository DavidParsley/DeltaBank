import { createContext, useEffect, useState } from "react";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
    
  const navigate = useNavigate();
  const [authToken, setAuthToken] = useState(() =>
    sessionStorage.getItem("token")
  );

  const [current_user, setCurrentUser] = useState(null);
  const [current_admin, setCurrentAdmin] = useState(null);
  const [users, setUsers] = useState([])
  // const [onChange, setOnChange] = useState(true);

// LOGIN
  const login = (email, password) => {
    toast.loading("Logging you in ... ");
    fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify({ email, password }),
    })
      .then((resp) => resp.json())
      .then((response) => {
        if (response.access_token) {
          toast.dismiss();
          sessionStorage.setItem("token", response.access_token);
          setAuthToken(response.access_token);

          fetch("http://127.0.0.1:5000/current_user", {
            method: "GET",
            headers: {
              "Content-type": "application/json",
              Authorization: `Bearer ${response.access_token}`,
            },
          })
            .then((response) => response.json())
            .then((response) => {
              console.log(response); 

              if (response.is_admin) {
                setCurrentAdmin(response); 
              } else {
                setCurrentUser(response);               }
            });

          toast.success("Successfully Logged in");
          navigate("/");
        } else if (response.error) {
          toast.dismiss();
          toast.error(response.error);
        } else {
          toast.dismiss();
          toast.error("Failed to login");
        }
      });
  };


  // LOG OUT
  const logout = () => {
    toast.loading("Logging out ... ");
    fetch("http://127.0.0.1:5000/logout", {
      method: "DELETE",
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${authToken}`,
      },
    })
      .then((resp) => resp.json())
      .then((response) => {
        console.log(response);

        if (response.success) {
          sessionStorage.removeItem("token");
          setAuthToken(null);
          setCurrentUser(null);
          setCurrentAdmin(null);

          toast.dismiss();
          toast.success("Successfully Logged out");

          navigate("/");
        }
      });
  };




















































































}