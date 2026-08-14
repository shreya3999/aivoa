import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  loading: false,
  error: null,

  complaint: {
    complaint_source: "",
    customer_name: "",
    customer_email: "",
    customer_country: "",

    product_name: "",
    product_code: "",
    product_strength: "",
    batch_number: "",
    manufacturing_date: "",
    expiry_date: "",
    quantity_affected: "",

    complaint_type: "",
    complaint_date: "",
    detailed_complaint_description: "",

    initial_severity: "",
    priority: "",
  },

  completeness: {
    status: "",
    missing_fields: [],
  },

  risk: {
    risk_level: "",
    reason: "",
  },

  recommendations: [],
};


const complaintSlice = createSlice({

  name: "complaint",

  initialState,

  reducers: {

    setLoading: (state, action) => {
      state.loading = action.payload;
    },

    setError: (state, action) => {
      state.error = action.payload;
    },

    setComplaint: (state, action) => {

      state.complaint = {
        ...state.complaint,
        ...action.payload,
      };

    },

    setAnalysisResult: (state, action) => {

      state.complaint = {
        ...state.complaint,
        ...(action.payload.complaint || {}),
      };

      state.completeness =
        action.payload.completeness || {
          status: "",
          missing_fields: [],
        };

      state.risk =
        action.payload.risk_assessment || {
          risk_level: "",
          reason: "",
        };

      state.recommendations =
        action.payload.recommendations || [];

    },

    resetComplaint: () => initialState,

  },

});


export const {
  setLoading,
  setError,
  setComplaint,
  setAnalysisResult,
  resetComplaint,
} = complaintSlice.actions;


export default complaintSlice.reducer;