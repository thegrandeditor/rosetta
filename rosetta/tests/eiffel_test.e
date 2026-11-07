class ACCOUNT
feature
  balance: INTEGER
  
  make (initial_balance: INTEGER)
    require
      initial_balance >= 0
    do
      balance := initial_balance
    ensure
      balance = initial_balance
    end

  withdraw (amount: INTEGER)
    require
      amount > 0
      amount <= balance
    do
      balance := balance - amount
    ensure
      balance = old balance - amount
    end

invariant
  balance >= 0
end
