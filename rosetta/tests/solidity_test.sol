contract SimpleBank {
    mapping(address => uint) balances;
    event Transfer(address indexed from, address indexed to, uint amount);
    
    function deposit(uint amount) public payable {
        balances[msg.sender] = balances[msg.sender] + amount;
        emit Transfer(address(0), msg.sender, amount);
    }
}
