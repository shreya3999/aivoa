import Header from "../../frontend/src/components/header";

import FileUpload from "../../frontend/src/components/FileUpload";

import ComplaintForm from "../../frontend/src/components/ComplaintForm";

import RiskAssessment from "../../frontend/src/components/RiskAssessment";

import { useSelector } from "react-redux";


function App() {

  const error = useSelector(
    (state) => state.complaint.error
  );


  return (

    <div className="app">

      <Header />


      <main className="container">


        {/* Page heading */}

        <div className="page-heading">

          <div>

            <span className="section-label">
              QUALITY MANAGEMENT SYSTEM
            </span>

            <h1>
              Customer Complaint Management
            </h1>

            <p>
              AI-powered complaint intake,
              assessment and investigation support.
            </p>

          </div>

        </div>


        {/* Upload */}

        <FileUpload />


        {/* Error */}

        {error && (

          <div className="error-message">
            {error}
          </div>

        )}


        {/* Main workspace */}

        <div className="workspace">


          {/* Left */}

          <div>

            <ComplaintForm />

          </div>


          {/* Right */}

          <div>

            <RiskAssessment />

          </div>


        </div>

      </main>

    </div>
  );
}


export default App;