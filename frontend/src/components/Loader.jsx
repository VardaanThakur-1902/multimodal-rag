const Loader = () => {
  return (
    <div className="flex items-center gap-2 p-4">

      <div className="h-2 w-2 rounded-full bg-white animate-bounce"></div>

      <div
        className="h-2 w-2 rounded-full bg-white animate-bounce"
        style={{ animationDelay: "0.2s" }}
      ></div>

      <div
        className="h-2 w-2 rounded-full bg-white animate-bounce"
        style={{ animationDelay: "0.4s" }}
      ></div>

    </div>
  );
};

export default Loader;