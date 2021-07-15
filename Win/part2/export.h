#pragma once

// Define CLIENT_SDK for any platform
#if defined _WIN32 || defined __CYGWIN__
  #ifdef C_API_EXPORT
    // Exporting...
    #ifdef __GNUC__
      #define C_SDK_EXPORTED __attribute__ ((dllexport))
    #else
      #define C_SDK_EXPORTED __declspec(dllexport) // Note: actually gcc seems to also supports this syntax.
    #endif
  #else
    #ifdef __GNUC__
      #define C_SDK_EXPORTED __attribute__ ((dllimport))
    #else
      #define C_SDK_EXPORTED __declspec(dllimport) // Note: actually gcc seems to also supports this syntax.
    #endif
  #endif
  #define NOT_EXPORTED
#else
  #if __GNUC__ >= 4
    #define C_SDK_EXPORTED __attribute__ ((visibility ("default")))
    #define NOT_EXPORTED  __attribute__ ((visibility ("hidden")))
  #else
    #define C_SDK_EXPORTED
    #define NOT_EXPORTED
  #endif
#endif
