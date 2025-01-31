import { React , useContext, useState } from 'react';
import { Link } from "react-router-dom";
import { UserContext } from "../context/UserContext";

export default function Register() {
  
  const { addUser } = useContext(UserContext);

  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  function handleSubmit(e) {
    e.preventDefault()
    if (password != repeatPassword) return alert("Password doesnt match");
    else addUser(first_name, last_name, phone, email, password);
  }

  return (
    <div className="Register-form font-[sans-serif] max-w-4xl flex items-center mx-auto  p-4 mt-15">
      <div className="grid md:grid-cols-3 gap-6 items-center shadow-[0_2px_10px_-3px_rgba(6,81,237,0.3)] rounded-xl ">
        <div className="Register-form-text max-md:order-1 flex flex-col justify-center md:space-y-16 space-y-8 max-md:mt-16 min-h-full b lg:px-8 px-4 py-4">
          <div>
            <h4 className="text-lg">Create Your Account</h4>
            <p className="text-[14px] mt-3 leading-relaxed">
              Welcome to our registration page! Get started by creating your
              account.
            </p>
          </div>
          <div>
            <h4 className="text-lg">Simple & Secure Registration</h4>
            <p className="text-[14px] mt-3 leading-relaxed">
              Our registration process is designed to be straightforward and
              secure. We prioritize your privacy and data security.
            </p>
          </div>
        </div>

        <form
          onSubmit={handleSubmit}
          className="md:col-span-2 w-full py-6 px-6 sm:px-16 max-md:max-w-xl mx-auto"
        >
          <div className="mb-6">
            <h3 className="text-gray-800 text-xl font-bold">
              Create an account
            </h3>
          </div>

          <div className="space-y-6">
            <div>
              <label className="text-gray-600 text-sm mb-2 block">
                First Name
              </label>
              <div className="relative flex items-center">
                <input
                  type="text"
                  value={first_name}
                  onChange={(e) => setFirstName(e.target.value)}
                  required
                  className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                  placeholder="Enter first name"
                />
              </div>
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">
                Last Name
              </label>
              <div className="relative flex items-center">
                <input
                  type="text"
                  value={last_name}
                  onChange={(e) => setLastName(e.target.value)}
                  required
                  className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                  placeholder="Enter last name"
                />
              </div>
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Phone</label>
              <div className="relative flex items-center">
                <input
                  type="number"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  required
                  className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                  placeholder="Enter phone number"
                />
              </div>
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">Email</label>
              <div className="relative flex items-center">
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                  placeholder="Enter email"
                />
              </div>
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">
                Password
              </label>
              <div className="relative flex items-center">
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                  placeholder="Enter password"
                />
              </div>
            </div>

            <div>
              <label className="text-gray-600 text-sm mb-2 block">
                {" "}
                Repeat Password
              </label>
              <div className="relative flex items-center">
                <input
                  type="password"
                  value={repeatPassword}
                  onChange={(e)=>setRepeatPassword(e.target.value)}
                  required
                  className="text-gray-800 bg-white border border-gray-300 w-full text-sm pl-4 pr-8 py-2.5 rounded-md outline-blue-500"
                  placeholder="Enter password"
                />
              </div>
            </div>

            {/* <div className="flex items-center">
              <input id="remember-me" name="remember-me" type="checkbox" className="h-4 w-4 shrink-0 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" />
              <label htmlFor="remember-me" className="ml-3 block text-sm text-gray-600">
                I accept the <a href="javascript:void(0);" className="text-blue-600 font-semibold hover:underline ml-1">Terms and Conditions</a>
              </label>
            </div> */}
          </div>

          <div className="mt-8">
            <button
              type="submit"
              className="w-full py-2.5 px-4 tracking-wider text-sm rounded-md text-black bg-[#d0f500d7]  hover:bg-purple-700 focus:outline-none"
            >
              Create an account
            </button>
          </div>
          <p className="text-black text-sm mt-6 text-center">
            Already have an account?{" "}
            <Link to ="/login"
              className="text-purple-600 font-semibold hover:underline ml-1"
            >
              Login here
            </Link>
          </p>
        </form>
      </div>
    </div>
  );
}
