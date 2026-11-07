MODULE Hello;
  FROM InOut IMPORT WriteString, WriteLn;
  CONST
    Greeting = "Hello, Modula-2!";
  VAR
    i: INTEGER;
  
  PROCEDURE Greet(n: INTEGER);
  BEGIN
    FOR i := 1 TO n DO
      WriteString(Greeting);
      WriteLn;
    END;
  END Greet;

BEGIN
  Greet(5);
END Hello.
