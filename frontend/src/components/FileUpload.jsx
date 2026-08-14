import { useDispatch, useSelector } from "react-redux";

import axios from "axios";

import {
  setLoading,
  setError,
  setAnalysisResult,
} from "../redux/complaintSlice";


function FileUpload() {

  const dispatch = useDispatch();

  const loading = useSelector(
    (state) => state.complaint.loading
  );


  const handleFileChange = async (event) => {

    const file = event.target.files[0];

    if (!file) {
      return;
    }


    const formData = new FormData();

    formData.append(
      "file",
      file
    );


    try {

      dispatch(
        setLoading(true)
      );

      dispatch(
        setError(null)
      );


      const response =
        await axios.post(

          "http://127.0.0.1:8000/api/complaints/analyze",

          formData,

          {
            headers: {
              "Content-Type":
                "multipart/form-data",
            },
          }
        );


      dispatch(
        setAnalysisResult(
          response.data
        )
      );


    } catch (error) {

      console.error(error);

      dispatch(
        setError(
          error.response?.data?.detail ||
          "Unable to analyze complaint"
        )
      );

    } finally {

      dispatch(
        setLoading(false)
      );

    }
  };


  return (

    <div className="upload-card">

      <div className="upload-icon">
        ↑
      </div>

      <h2>
        Upload Customer Complaint
      </h2>

      <p>
        Upload a complaint PDF or text file.
        AI will extract and assess the complaint.
      </p>


      <label className="upload-button">

        {loading
          ? "Analyzing..."
          : "Choose Complaint File"}

        <input
          type="file"
          accept=".pdf,.txt"
          onChange={handleFileChange}
          disabled={loading}
          hidden
        />

      </label>


      <span className="upload-help">
        Supported formats: PDF, TXT
      </span>

    </div>
  );
}

export default FileUpload;