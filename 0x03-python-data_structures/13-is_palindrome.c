#include <stdio.h>
#include "lists.h"
/**
 * reverse - reverses the second half of the list
 * @head: head of the second half
 * Return: no return
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * compare - compares each int of the list
 *
 * @head1: head of the first half
 * @head2: head of the second half
 * Return: 1 if are equals, 0 if not
 */
int compare(listint_t *head1, listint_t *head2)
{
	while (head1 && head2)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}
	return (1);
}
/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	listint_t *prev_of_slow = *head;
	listint_t *mid = NULL
	int is_palindrome = 1;

if (*head != NULL && (*head)->next != NULL)
{
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_of_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	second_half = reverse(slow);
	prev_of_slow->next = second_half;
	is_palindrome = compare(*head, second_half);
	second_half = reverse(second_half);
	prev_of_slow->next = mid;
	if (mid != NULL)
		mid->next = second_half;
	else
		prev_of_slow->next = second_half;
}
return (is_palindrome);
}
