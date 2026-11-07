WITH Ada.Text_IO; USE Ada.Text_IO;
PROCEDURE Hello IS
   Sum : Integer := 0;
BEGIN
   FOR I IN 1 .. 10 LOOP
      Sum := Sum + I;
   END LOOP;
   Put_Line("Sum is " & Integer'Image(Sum));
END Hello;
