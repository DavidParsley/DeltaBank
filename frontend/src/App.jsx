import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom"; 
import { LoanProvider } from "./context/LoanContext";
import { UserProvider } from "./context/UserContext"
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import NoPage from "./pages/NoPage";
import Register from "./pages/Register";
import Profile from "./pages/Profile";
import SingleLoan from "./pages/SingleLoan";
import AddLoan from "./pages/AddLoan";
import About from "./pages/About";
import Accounts from "./pages/Accounts";

function App() {
  return (
    <BrowserRouter>
      <UserProvider>
        <LoanProvider>
          <Routes>
            <Route path="/" element={<Layout />}>
              <Route index element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/about" element={<About />} />
              <Route path="/profile" element={<Profile />} />
              <Route path="/accounts" element={<Accounts />} />
              <Route path="/register" element={<Register />} />
              <Route path="/singleloan/:id" element={<SingleLoan />} />
              <Route path="/addloan" element={<AddLoan />} />
              <Route path="*" element={<NoPage />} />
            </Route>
          </Routes>
        </LoanProvider>
      </UserProvider>
    </BrowserRouter>
  );
}

export default App;
