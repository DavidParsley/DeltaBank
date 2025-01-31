import React from "react";

export default function About() {
  return (
    <div className="about-container">
      {/* Main Title */}
      <h1 className="about-title">About Delta Bank</h1>
      <br />

      {/* Introduction Section */}
      <section className="about-section intro-section">
        <h2 className="section-title">Delta Bank</h2>
        <p className="section-content">
          Delta Bank is a web application designed to streamline the operations
          of a bank by connecting users and admins within a unified platform.
          The system enables users to self-register, manage their personal
          account details, and view their loans. Admins, once logged in, can
          manage and oversee all loans in the database, update loan statuses,
          and delete users along with their loans. Secure authentication ensures
          that only authorized users can access sensitive data, with users being
          restricted to their own data and admins having full control over the
          system's loan management features.
        </p>
      </section>
      <br />

      {/* Problem Statement Section */}
      <section className="about-section problem-section">
        <h2 className="section-title">Problem Statement</h2>
        <p className="section-content">
          Managing a bank’s operations can be complex, especially with a large
          number of users and loans. Ensuring that only authorized users can
          access sensitive information, such as loan records, is crucial for
          maintaining data security and privacy. The Delta Bank system aims to
          simplify and centralize these operations by offering a user-friendly
          platform where users can self-register, view their loans, and update
          their details, while admins can manage loans, assign them to users,
          and handle account deletions in a secure environment.
        </p>
      </section>
      <br />

      {/* Solution Section */}
      <section className="about-section solution-section">
        <h2 className="section-title">Proposed Solution</h2>
        <p className="section-content">
          Delta Bank makes managing your bank account and loans simple and
          secure. Here’s how:
          <ul>
            <li>
              <strong>Easy Sign-Up:</strong> Users can quickly create an account
              and start managing their loans.
            </li>
            <li>
              <strong>Loan Management:</strong> View your loans, check the
              status, and update details anytime.
            </li>
            <li>
              <strong>Safe & Secure:</strong> Login securely to protect your
              account and sensitive data.
            </li>
            <li>
              <strong>Admin Control:</strong> Admins can manage loans and user
              accounts to ensure everything runs smoothly.
            </li>
          </ul>
        </p>
      </section>
      <br />

      {/* Future Plans Section */}
      <section className="about-section future-section">
        <h2 className="section-title">Future Plans</h2>
        <p className="section-content">
          The platform will continue to grow with additional features such as
          detailed reporting tools, more user management options, and support
          for future integrations. We plan to enhance the user experience and
          increase the scalability of the platform to accommodate more users,
          more loans, and more advanced functionalities.
        </p>
      </section>
      <br />
      <br />
    </div>
  );
}
