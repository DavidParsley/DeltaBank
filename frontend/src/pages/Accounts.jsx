import React, { useContext, useState } from "react";
import { UserContext } from "../context/UserContext";
import { toast } from "react-toastify";

export default function Accounts() {
  const { users, deleteUser } = useContext(UserContext);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedUserId, setSelectedUserId] = useState(null);


  const openDeleteModal = (userId) => {
    setSelectedUserId(userId);
    setIsModalOpen(true);
  };

  
  const closeDeleteModal = () => {
    setIsModalOpen(false);
    setSelectedUserId(null);
  };

  
  const handleDelete = () => {
    if (selectedUserId) {
      deleteUser(selectedUserId); 
      closeDeleteModal(); 
    } else {
      toast.error("User not found");
    }
  };

  return (
    <div className="loan-cards-container mt-8 p-8" style={{ backgroundColor: "#f4f7f9" }}>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* User Cards */}
        {users &&
          users.map((user) => (
            <div key={user.id} className="flex items-center justify-center p-4">
              <div
                className="w-full max-w-3xl rounded-2xl overflow-hidden shadow-xl transition-transform transform hover:scale-105"
                style={{ backgroundColor: "#ffffff", boxShadow: "0 2px 10px rgba(0, 0, 0, 0.1)" }}
              >
                <div className="px-8 py-10">
                  <div className="text-center mb-8">
                    <img
                      className="w-24 h-24 rounded-full border-2 border-gray-300 mx-auto mb-6"
                      src={`https://ui-avatars.com/api/?name=${user.first_name}+${user.last_name}&background=random`}
                      alt="user photo"
                    />
                    <h3 className="font-semibold text-3xl text-gray-900 hover:text-gray-600 transition-colors duration-300">
                      {user.first_name} {user.last_name}
                    </h3>
                  </div>

                  <div className="text-gray-800">
                    <div className="mb-6">
                      <span className="font-medium text-lg text-gray-600">Phone:</span>
                      <p className="text-lg font-semibold text-gray-900">{user.phone}</p>
                    </div>
                    <div className="mb-6">
                      <span className="font-medium text-lg text-gray-600">Email:</span>
                      <p className="text-lg font-semibold text-gray-900">{user.email}</p>
                    </div>
                  </div>
                </div>

                <div className="px-8 pb-8">
                  <button
                    onClick={() => openDeleteModal(user.id)} // Open modal with user.id
                    className="w-full rounded-lg text-white font-semibold py-3 bg-black shadow-md hover:bg-red-600 transition-colors duration-300"
                  >
                    Delete Account
                  </button>
                </div>
              </div>
            </div>
          ))}
      </div>

      {/* Modal for delete confirmation */}
      {isModalOpen && (
        <div className="modal fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-xl max-w-sm w-full">
            <h2 className="text-xl font-semibold mb-4">Are you sure you want to delete this account?</h2>
            <div className="flex justify-end gap-4">
              <button
                onClick={closeDeleteModal}
                className="px-4 py-2 bg-gray-300 rounded-lg"
              >
                Cancel
              </button>
              <button
                onClick={handleDelete}
                className="px-4 py-2 bg-red-600 text-white rounded-lg"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
