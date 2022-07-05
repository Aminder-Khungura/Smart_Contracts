# Needed at the start to know which compiler version your contract needs
pragma solidity 0.8.7;

# Define smart contract
contract MyContract {
    mapping(address => uint) private balances;

    # Define function that receive money
    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    # Define function to withdraw money
    function withdraw(address payable addr, unit amount) public payable {
        # Check if balance is greater then amount
        require(balances[addr] >= amount);
        # Send money
        (bool sent, bytes memory data) = addr.call{value: amount}("");
        # Check if money sent
        require(sent, "Could not withdraw");
        # Update balance
        balances[msg.sender] -= amount;
    }
    # Define function that gets the balance
    function getBalance() public view returns (uint) {
        # address is casting "this", which refers to the contract itself, to an address.
        return address(this).balance;
    }
}