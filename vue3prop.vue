export default {
    props: {
      // Basic type check
      //  (`null` and `undefined` values will allow any type)
      propA: Number,
      // Multiple possible types
      propB: [String, Number],
      // Required string
      propC: {
        type: String,
        required: true
      },
      // Number with a default value
      propD: {
        type: Number,
        default: 100
      },
      // Object with a default value
      propE: {
        type: Object,
        // Object or array defaults must be returned from
        // a factory function. The function receives the raw
        // props received by the component as the argument.
        default(rawProps) {
          return { message: 'hello' }
        }
      },
      // Custom validator function
      propF: {
        validator(value) {
          // The value must match one of these strings
          return ['success', 'warning', 'danger'].includes(value)
        }
      },
      // Function with a default value
      propG: {
        type: Function,
        // Unlike object or array default, this is not a factory 
        // function - this is a function to serve as a default value
        default() {
          return 'Default function'
        }
      }
    }
  }