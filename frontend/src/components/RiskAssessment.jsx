import { useSelector } from "react-redux";


function RiskAssessment() {

  const {
    risk,
    completeness,
    recommendations,
  } = useSelector(
    (state) => state.complaint
  );


  const getRiskClass = () => {

    switch (
      risk.risk_level?.toUpperCase()
    ) {

      case "CRITICAL":
        return "risk-critical";

      case "HIGH":
        return "risk-high";

      case "MEDIUM":
        return "risk-medium";

      case "LOW":
        return "risk-low";

      default:
        return "risk-none";
    }
  };


  return (

    <div className="ai-panel">


      {/* Header */}

      <div className="ai-panel-header">

        <div>

          <span className="section-label">
            AI COPILOT
          </span>

          <h2>
            Risk Assessment
          </h2>

        </div>

        <div className="sparkle">
          ✦
        </div>

      </div>


      {/* Risk */}

      <div className="risk-box">

        <span>
          RISK LEVEL
        </span>


        <div
          className={`risk-level ${getRiskClass()}`}
        >
          {risk.risk_level ||
            "Not Assessed"}
        </div>

      </div>


      {/* Reason */}

      <div className="ai-section">

        <h3>
          Why this risk?
        </h3>

        <p>
          {risk.reason ||
            "Upload a complaint to generate an AI risk assessment."}
        </p>

      </div>


      {/* Completeness */}

      <div className="ai-section">

        <h3>
          Complaint Completeness
        </h3>

        <div className="completeness">

          <span>
            {completeness.status ||
              "Not Checked"}
          </span>

          {completeness.missing_fields
            ?.length > 0 && (

            <div className="missing">

              Missing:

              {completeness.missing_fields.map(
                (field) => (

                  <span key={field}>
                    {field}
                  </span>

                )
              )}

            </div>

          )}

        </div>

      </div>


      {/* Recommendations */}

      <div className="ai-section">

        <h3>
          AI Recommendations
        </h3>


        {recommendations.length === 0 ? (

          <p>
            Recommendations will appear
            after AI analysis.
          </p>

        ) : (

          <ol className="recommendations">

            {recommendations.map(
              (recommendation, index) => (

                <li key={index}>
                  {recommendation}
                </li>

              )
            )}

          </ol>

        )}

      </div>

    </div>
  );
}

export default RiskAssessment;