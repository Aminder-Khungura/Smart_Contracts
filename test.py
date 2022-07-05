# Needed at the start to know which compiler version your contract needs
pragma solidity 0.8.7;

# Define smart contract
contract MyContract {
    uint public x = 21;

    # Define public function
    function setX(uint y) public {
        x = y;
    }

    # Define function that uses mapping (which is basically a Dictionary in Python)
    function setKey(uint key, int value) public {
        map[key] = value;
    }

    # create variable to hold address of last person who sent ETH
    address public lastSender;

    # Define function that receive money, external mean this function can only be called from outside this contract
    function recieve() external payable {
        lastSender = msg.sender;
    }

    # Define function that gets the balance of the contract, view means this function is read only
    function getBalance() public view returns (uint) {
        # address is casting "this", which refers to the contract itself, to an address.
        return address(this).balance;
    }

    # Define function to send ETH
    function pay(address payable addr) public payable {
        # Don't use these:
        addr.trasnfer()
        addr.send()
        # Use
        (bool sent, bytes memory data) = addr.call{value: 1 ether}(""); "Amount of ETH you want to send"
        # Use require to check if money was sent
        require(sent, "Error sending money");

    }
}