import { useDispatch, useSelector } from "react-redux";

import {
  setComplaint,
} from "../redux/complaintSlice";


function ComplaintForm() {

  const dispatch = useDispatch();


  const complaint = useSelector(
    (state) =>
      state.complaint.complaint
  );


  const handleChange = (event) => {

    const {
      name,
      value,
    } = event.target;


    dispatch(
      setComplaint({
        [name]: value,
      })
    );
  };


  return (

    <div className="card">

      <div className="card-header">

        <div>

          <span className="section-label">
            CUSTOMER COMPLAINT
          </span>

          <h2>
            Log Customer Complaint
          </h2>

        </div>

        <span className="ai-badge">
          AI POPULATED
        </span>

      </div>


      <div className="form-grid">


        {/* Customer */}

        <div className="form-section">

          <h3>
            Customer Details
          </h3>


          <label>
            Complaint Source

            <input
              name="complaint_source"
              value={
                complaint.complaint_source
              }
              onChange={handleChange}
              placeholder="Email / Phone / Portal"
            />

          </label>


          <label>
            Customer Name

            <input
              name="customer_name"
              value={
                complaint.customer_name
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Customer Email

            <input
              name="customer_email"
              value={
                complaint.customer_email
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Country

            <input
              name="customer_country"
              value={
                complaint.customer_country
              }
              onChange={handleChange}
            />

          </label>

        </div>


        {/* Product */}

        <div className="form-section">

          <h3>
            Product & Batch
          </h3>


          <label>
            Product Name

            <input
              name="product_name"
              value={
                complaint.product_name
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Product Code

            <input
              name="product_code"
              value={
                complaint.product_code
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Product Strength

            <input
              name="product_strength"
              value={
                complaint.product_strength
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Batch Number

            <input
              name="batch_number"
              value={
                complaint.batch_number
              }
              onChange={handleChange}
            />

          </label>

        </div>


        {/* Dates */}

        <div className="form-section">

          <h3>
            Manufacturing Details
          </h3>


          <label>
            Manufacturing Date

            <input
              name="manufacturing_date"
              value={
                complaint.manufacturing_date
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Expiry Date

            <input
              name="expiry_date"
              value={
                complaint.expiry_date
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Quantity Affected

            <input
              type="number"
              name="quantity_affected"
              value={
                complaint.quantity_affected
              }
              onChange={handleChange}
            />

          </label>

        </div>


        {/* Complaint */}

        <div className="form-section">

          <h3>
            Complaint Details
          </h3>


          <label>
            Complaint Type

            <input
              name="complaint_type"
              value={
                complaint.complaint_type
              }
              onChange={handleChange}
            />

          </label>


          <label>
            Complaint Date

            <input
              name="complaint_date"
              value={
                complaint.complaint_date
              }
              onChange={handleChange}
            />

          </label>


          <label className="full-width">
            Detailed Description

            <textarea
              name="detailed_complaint_description"
              value={
                complaint.detailed_complaint_description
              }
              onChange={handleChange}
              rows="5"
            />

          </label>

        </div>


      </div>

    </div>
  );
}

export default ComplaintForm;